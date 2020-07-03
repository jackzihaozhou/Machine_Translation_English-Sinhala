#!/usr/bin/env bash
#SBATCH --mem=8G
#SBATCH --gres=gpu:1
#SBATCH -t 0

python baseline/translate.py \
    --cuda \
    --src en \
    --tgt si \
    --model-file en-si-multi.pt \
    --search "beam_search" \
    --beam-size 5 \
    --n-layers 5 \
    --input-file assignment2/data/en_si/ensi_parallel.bpe.dev.en \
    --output-file ensi_parallel.dev.out.si
