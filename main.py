from data import fetch
from data import preprocess
from data import aggregate

from model import tune
from model import train
from model import predict

#from output import write
#from output import score

def main():
    raw_dict = fetch.main()
    eng_dict, pred_df = preprocess.main(raw_dict)
    mega_df = aggregate.main(eng_dict)

    params = tune.main(mega_df)
    model = train.main(params)
    predictions = predict.main(model, pred_df)

    #write.main()

    #score.main()

if __name__ == '__main__':
    main() 