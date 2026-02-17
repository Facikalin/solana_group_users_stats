from dex_client import get_best_pair, get_pair_detail, calculate_simple_roi

# BURAYA TEST TOKEN CA YAZ
ca = "8SMMso8Muv8d6i4WmMDthKt6TN1ysN6937sx3DKLXZqB"

pair = get_best_pair(ca)

if not pair:
    print("Pair bulunamadı")
else:
    pair_address = pair.get("pairAddress")
    print("Seçilen DEX:", pair.get("dexId"))
    print("Pair Address:", pair_address)

    pair_detail = get_pair_detail(pair_address)

    if not pair_detail:
        print("Pair detail alınamadı")
    else:
        result = calculate_simple_roi(pair_detail)

        if not result:
            print("ROI hesaplanamadı")
        else:
            print("\n--- ROI SONUÇ ---")
            print("24h Önceki Tahmini Fiyat:", result["first_price_estimate"])
            print("Güncel Fiyat:", result["current_price"])
            print("ROI (24h):", round(result["roi"], 2), "x")
