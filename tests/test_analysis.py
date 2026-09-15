from src.analysis import load_and_clean

def test_load_and_clean():
    df = load_and_clean("data/sales.csv")
    assert not df.empty
    assert "revenue" in df.columns
    assert "profit" in df.columns
    assert (df["quantity"] > 0).all()
