from data import fetch
from data import preprocess
from data import aggregate
from model import tune
from model import train
from model import predict
from model import write

from output import score

def main():
    data = fetch.main()

    eng_data = preprocess.main(data)
    mega_df = aggregate.main(eng_data)

    tune.main()

    train.main()

    predict.main()

    write.main()

    score.main()

if __name__ == '__main__':
    main() 