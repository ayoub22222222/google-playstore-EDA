from src.data_preprocessing import load_data, cleaned_data, save_data_to_csv 


def main():

    # load files

    df = load_data('~/google-playstore-EDA/data/googleplaystore.csv')
    print("wait please")

    # clean it
    cl = cleaned_data(df)

    # save it

    save_data_to_csv(cl, '~/google-playstore-EDA/data/test.csv')
    print("data stored")


if __name__ == "__main__":
    main()
