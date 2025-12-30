from data import fetch
from data import preprocess
from data import aggregate
#from model import tune
#from model import train
#from model import predict
#from model import write

#from output import score

def main():
    raw_dict = fetch.main()
    eng_dict = preprocess.main(raw_dict)
    mega_df = aggregate.main(eng_dict)

    #tune.main()
    #train.main()
    #predict.main()

    #write.main()

    #score.main()

if __name__ == '__main__':
    main() 