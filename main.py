from src.data import fetch
from src.data import preprocess
from src.data import aggregate

from src.model import tune
from src.model import predict

#from src.output import write
#from src.output import score

def main():
    raw_dict = fetch.main()
    eng_dict, pred_df = preprocess.main(raw_dict)
    mega_df = aggregate.main(eng_dict)

    mega_df.to_csv('mega_df.csv')
    pred_df.to_csv('pred_df.csv')

    model = tune.main(mega_df)['model']
    predictions = predict.main(model, pred_df)

    #write.main()

    #score.main()

if __name__ == '__main__':
    main() 