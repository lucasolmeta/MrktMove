def main():
    df = df.sort_values(date_col)
    cutoff = df[date_col].iloc[-val_days]
    train = df[df[date_col] < cutoff]
    val = df[df[date_col] >= cutoff]
    return train, val

if __name__ == '__main__':
    main()