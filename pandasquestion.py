#checking student eligibility

def eligible_for_graduation(df):
    return df[(df['credits'] >= 120) & (df['courses'] >= 30)]