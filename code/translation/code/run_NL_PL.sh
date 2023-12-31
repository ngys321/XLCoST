#!/usr/bin/env bash


source common_run_utils.sh
PATH_DATA_PREFIX=${ROOT_PATH}g4g/XLCoST_data/


# bash run_NL_PL.sh 2 java desc program graphcodebert train
# bash run_NL_PL.sh 2 desc python program graphcodebert eval
# bash run_NL_PL.sh 2 comment python snippet graphcodebert train
# bash run_NL_PL.sh 2 java comment snippet graphcodebert eval
GPU=${1:-0};
SOURCE=${2:-java};
TARGET=${3:-python};
DATA_TYPE=${4:-snippet};
MODEL=${5:-codebert};
IS_TRAIN=${6:-train};
NUM_EPOCHS=${7:-10};
pretrained_model="microsoft/codebert-base";
model_type="roberta";
beam_size=5;
num_train_epochs=$NUM_EPOCHS;

if [[ $MODEL == 'codebert' ]]; then
    pretrained_model="microsoft/codebert-base";
elif [[ $MODEL == 'roberta' ]]; then
    pretrained_model="roberta-base";
elif [[ $MODEL == 'graphcodebert' ]]; then
    pretrained_model="microsoft/graphcodebert-base";
elif [[ $MODEL == 'codet5' ]]; then
    pretrained_model="Salesforce/codet5-base";
    model_type=$MODEL
elif [[ $MODEL == 'bart' ]]; then
    pretrained_model="facebook/bart-base";
    model_type=$MODEL
elif [[ $MODEL == 'plbart' ]]; then
    pretrained_model="uclanlp/plbart-base"; # uclanlp/plbart-base    uclanlp/plbart-python-en_XX
    model_type=$MODEL
elif [[ $MODEL == 'codet5p' ]]; then
    pretrained_model="Salesforce/codet5p-220m";
    model_type=$MODEL
elif [[ $MODEL == 'unixcoder' ]]; then
    pretrained_model="microsoft/unixcoder-base";
fi

experiment_name=${MODEL}_nl_pl_${DATA_TYPE}
if [[ $TARGET == 'desc' ]] || [[ $TARGET == 'comment' ]]; then
    experiment_name=${MODEL}_pl_nl_${DATA_TYPE}

fi


PATH_DATA=${PATH_DATA_PREFIX}pair_data_tok_1_comment/;

source_length=100;
target_length=100;
TRAIN_STEPS=10000
EVAL_STEPS=5000
TRAIN_BATCH_SIZE=32
EVAL_BATCH_SIZE=32

if [[ $DATA_TYPE == 'program' ]]; then
    source_length=400;
    target_length=400;
    if [[ $SOURCE == 'desc' ]]; then
        PATH_DATA=${PATH_DATA_PREFIX}pair_data_tok_full_desc_comment/; #pair_data_tok_full_desc
    elif [[ $TARGET == 'desc' ]]; then
        PATH_DATA=${PATH_DATA_PREFIX}pair_data_tok_full_desc/;
        target_length=100;
    fi
    TRAIN_STEPS=5000;
    EVAL_STEPS=2500;
    TRAIN_BATCH_SIZE=16
    EVAL_BATCH_SIZE=16
fi


#export CUDA_VISIBLE_DEVICES=$GPU
echo "Source: $SOURCE Target: $TARGET"
echo "Data path: $PATH_DATA"
echo "Pre-trained model: $pretrained_model"
echo "Model type: $model_type"
echo "Experiment name: $experiment_name"

SOURCE_LANG=${LANG_UPPER[$SOURCE]}
TARGET_LANG=${LANG_UPPER[$TARGET]}
LANG_PAIR=$SOURCE_LANG-$TARGET_LANG
PATH_2_DATA=${PATH_DATA}${LANG_PAIR}

if [ ! -d $PATH_2_DATA ] 
then
    LANG_PAIR=$TARGET_LANG-$SOURCE_LANG
    PATH_2_DATA=${PATH_DATA}${LANG_PAIR}
fi

SRC_FILE_SUFFIX=-$LANG_PAIR-tok${FILE_EXTENSION[$SOURCE_LANG]}
TGT_FILE_SUFFIX=-$LANG_PAIR-tok${FILE_EXTENSION[$TARGET_LANG]}
TRAIN_FILE_SRC=$PATH_2_DATA/train$SRC_FILE_SUFFIX
TRAIN_FILE_TGT=$PATH_2_DATA/train$TGT_FILE_SUFFIX
VAL_FILE_SRC=$PATH_2_DATA/val$SRC_FILE_SUFFIX
VAL_FILE_TGT=$PATH_2_DATA/val$TGT_FILE_SUFFIX
TEST_FILE_SRC=$PATH_2_DATA/test$SRC_FILE_SUFFIX
TEST_FILE_TGT=$PATH_2_DATA/test$TGT_FILE_SUFFIX
echo "TEST_FILE_SRC: $TEST_FILE_SRC TEST_FILE_TGT: $TEST_FILE_TGT"


SAVE_DIR=${CURRENT_DIR}/$experiment_name/$SOURCE_LANG-$TARGET_LANG
# SAVE_DIR=${CURRENT_DIR}/${DATA_SRC}/${SOURCE}2${TARGET};
mkdir -p $SAVE_DIR



function train () {


lr=5e-5;
GRAD_ACCUM_STEP=4; # We need to use 2 GPUs, batch_size_per_gpu=4

python run.py \
    --do_train \
    --do_eval \
    --model_type $model_type \
    --config_name $pretrained_model \
    --tokenizer_name $pretrained_model \
    --model_name_or_path $pretrained_model \
    --train_filename $TRAIN_FILE_SRC,$TRAIN_FILE_TGT \
    --dev_filename $VAL_FILE_SRC,$VAL_FILE_TGT \
    --output_dir $SAVE_DIR \
    --max_source_length $source_length \
    --max_target_length $target_length \
    --num_train_epochs $num_train_epochs \
    --train_steps $TRAIN_STEPS \
    --eval_steps $EVAL_STEPS \
    --train_batch_size $TRAIN_BATCH_SIZE \
    --eval_batch_size $EVAL_BATCH_SIZE \
    --beam_size $beam_size \
    --learning_rate $lr \

}

function train_from_cp () {
lr=5e-5;
GRAD_ACCUM_STEP=4; # We need to use 2 GPUs, batch_size_per_gpu=4
MODEL_PATH=${SAVE_DIR}/checkpoint-best-ppl/pytorch_model.bin;


python run.py \
    --do_train \
    --do_eval \
    --model_type $model_type \
    --config_name $pretrained_model \
    --tokenizer_name $pretrained_model \
    --model_name_or_path $pretrained_model \
    --load_model_path $MODEL_PATH \
    --train_filename $TRAIN_FILE_SRC,$TRAIN_FILE_TGT \
    --dev_filename $VAL_FILE_SRC,$VAL_FILE_TGT \
    --output_dir $SAVE_DIR \
    --max_source_length $source_length \
    --max_target_length $target_length \
    --num_train_epochs $num_train_epochs \
    --train_steps $TRAIN_STEPS \
    --eval_steps $EVAL_STEPS \
    --train_batch_size $TRAIN_BATCH_SIZE \
    --eval_batch_size $EVAL_BATCH_SIZE \
    --beam_size $beam_size \
    --learning_rate $lr \

}


function evaluate () {

GOUND_TRUTH_PATH=$PATH_2_DATA/test-${LANG_PAIR}-tok${FILE_EXTENSION[${LANG_UPPER[$TARGET]}]}
MODEL_PATH=${SAVE_DIR}/checkpoint-best-ppl/pytorch_model.bin;
RESULT_FILE=${SAVE_DIR}/result.txt;
SAVE_DIR1=${SAVE_DIR}
# MODEL_PATH=${SAVE_DIR}/checkpoint-best-bleu/pytorch_model.bin;
# SAVE_DIR1=${SAVE_DIR}/bleu
# mkdir -p $SAVE_DIR1
# RESULT_FILE1=${SAVE_DIR1}/result.txt;


python run.py \
    --do_test \
    --model_type $model_type \
    --model_name_or_path $pretrained_model \
    --config_name $pretrained_model \
    --tokenizer_name $pretrained_model  \
    --load_model_path $MODEL_PATH \
    --test_filename $TEST_FILE_SRC,$TEST_FILE_TGT \
    --output_dir $SAVE_DIR \
    --max_source_length $source_length \
    --max_target_length $target_length \
    --beam_size 5 \
    --eval_batch_size 16 \

python $evaluator_script/evaluator.py \
    --references $GOUND_TRUTH_PATH \
    --predictions $SAVE_DIR1/test_0.output \
    2>&1 | tee $RESULT_FILE;

# only 기능성에 대한 bleu 계산용. "in ㅇㅇㅇ programming paradigm" 빼고 저장. test_0_bleu_wo_paradigm.output, test_0_bleu_wo_paradigm.gold 에 저장.
python $evaluator_script/evaluator_wo_paradigm.py \
    --references  $SAVE_DIR1/test_0_bleu_wo_paradigm.gold \
    --predictions $SAVE_DIR1/test_0_bleu_wo_paradigm.output \
    2>&1 | tee $RESULT_FILE;

cd $codebleu_path;
python calc_code_bleu.py \
    --ref $GOUND_TRUTH_PATH \
    --hyp $SAVE_DIR1/test_0.output \
    --lang ${LANG_MAP[$TARGET]} \
    2>&1 | tee -a $RESULT_FILE1;
cd $CURRENT_DIR;

count=`ls -1 *.class 2>/dev/null | wc -l`;
[[ $count != 0 ]] && rm *.class;

}

if [[ $IS_TRAIN == 'train' ]]; then
    train;
fi
if [[ $IS_TRAIN == 'train_from_cp' ]]; then
    train_from_cp;
fi
evaluate;
# predict_transcoder_eval;
