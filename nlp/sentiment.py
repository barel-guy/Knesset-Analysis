from transformers import AutoTokenizer, AutoModel, pipeline
import pandas as pd
import torch

PROTOCOL_PATH = '..\data\knesset_protocols.csv'

def parse_csv(model):
    df = pd.read_csv(PROTOCOL_PATH)
    df['sentiment'] = add_sentiment(model,list(df['text'].apply(lambda s : s[:2048])))
    return df

def add_sentiment(model, sent):
    output = model(sent)
    labels = [o['label'] for o in output]
    return labels

def main(model):
    print("parsing csv...")
    df = parse_csv(model)
    print('saving dataframe to csv...')
    df.to_csv("..\data\knesset_protocols_sentiment.csv", index=False)
    print("done!")

def load_model():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'Using {device}')

    tokenizer = AutoTokenizer.from_pretrained("avichr/heBERT_sentiment_analysis") #same as 'avichr/heBERT' tokenizer
    model = AutoModel.from_pretrained("avichr/heBERT_sentiment_analysis")

    sentiment_analysis = pipeline(
        "sentiment-analysis",
        model="avichr/heBERT_sentiment_analysis",
        tokenizer="avichr/heBERT_sentiment_analysis",
        return_all_scores = False,
        device=0 if device.type == 'cuda' else -1
    )
    tokenizer_kwargs = {'padding': True,'truncation': True, 'max_length': 512}

    prediction = lambda x: sentiment_analysis(x, **tokenizer_kwargs)

    return prediction


if __name__ == "__main__":
    model = load_model()
    main(model)
