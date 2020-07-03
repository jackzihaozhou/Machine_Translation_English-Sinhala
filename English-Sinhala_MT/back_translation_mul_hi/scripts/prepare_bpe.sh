# Prepare BPE
for lang in si
do
    python baseline/subwords.py train \
    --model_prefix assignment2/data/${lang}_en/subwords \
    --vocab_size 8000 \
    --model_type bpe \
    --input assignment2/data/${lang}_en/${lang}en_parallel.train.$lang,assignment2/data/${lang}_en/${lang}en_parallel.train.en
done
# Apply BPE
for lang in si
do
    for split in train dev test
    do
        for l in $lang en
        do
            python baseline/subwords.py segment \
            --model assignment2/data/${lang}_en/subwords.model \
            < assignment2/data/${lang}_en/${lang}en_parallel.$split.$l \
            > assignment2/data/${lang}_en/${lang}en_parallel.bpe.$split.$l
        done
    done
done
