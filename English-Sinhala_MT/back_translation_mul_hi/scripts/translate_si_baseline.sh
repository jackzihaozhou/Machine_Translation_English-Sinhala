python3 baseline/translate.py \
    --cuda \
    --src si \
    --tgt en \
    --model-file si-en-multi-baseline.pt \
    --search "beam_search" \
    --beam-size 5 \
    --input-file assignment2/data/si_en/sien_parallel.bpe.dev.si \
    --output-file sien_parallel.dev.out.en
