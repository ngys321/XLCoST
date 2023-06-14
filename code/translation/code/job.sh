#!/bin/bash
# DOCS (sbatch, srun)
# https://github.com/dasandata/Open_HPC/blob/master/Document/User%20Guide/5_use_resource/5.2_Allocate_Resource.md

# HOW TO USE SBATCH
# gpu 4개, 사용시간은 48시간으로 지정하여 jop.sh 작업제출
# 참고 : --time=일-시간:분:초
# (base 파티션 & base_qos 인 경우) sbatch --gres=gpu:4 --time=48:00:00 ./job.sh
# (big 파티션 & big_qos 인 경우)  sbatch -p big -q big_qos --gres=gpu:4 --time=48:00:00 ./job.sh
# (cpu 파티션 & cpu_qos 인 경우) sbatch -p cpu -q cpu_qos --time=48:00:00 ./job.sh


# HOW TO USE SRUN
# gpu 4개, 사용시간은 48시간으로 지정하여 bash 실행
# srun --gres=gpu:4 --time=48:00:00 --pty bash -i

# HOW TO CHECH THE STATE OF SBATCH
# squeuelong -u ysnamgoong42

# HOW TO CANCEL THE JOB
# : YOU CAN SEE THE JOB ID NUMBER BY SQUEUELONG
# scancel {jobID number}

#################################################################################################

echo ""
echo ""
echo ""

echo "RUNNING SCRIPT: $SLURM_JOB_NAME"


#########################
# conda 환경 활성화.
source ~/.bashrc
conda activate xlcost
# cuda 11.7 환경 구성.
ml purge
ml load cuda/11.7
#########################

# GPU 체크
nvidia-smi
nvcc -V

######################################## 작업 준비 끝 ############################################
# 활성화된 환경에서 코드 실행.

# code generation
# bash run_NL_PL.sh 0 desc python program codet5p train 10
# bash run_NL_PL.sh 0 desc python program codet5p eval 10

# code summarization
bash run_NL_PL.sh 0 python desc program plbart train 10
bash run_NL_PL.sh 0 python desc program plbart eval 10
