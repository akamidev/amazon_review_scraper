from scraper import scrape_amazon_reviews
from database import insert_reviews, fetch_all_reviews

url = "https://www.amazon.fr/KREMA-Bonbons-tendres-R%C3%A9galad-framboise/dp/B07L8512GK?ref_=Oct_d_orecs_d_7637581031_5&pd_rd_w=zHLUj&content-id=amzn1.sym.7cbdc8bd-517e-40af-8cf6-d59131f19899&pf_rd_p=7cbdc8bd-517e-40af-8cf6-d59131f19899&pf_rd_r=3N8M97ECDJ2ENP0MTK2P&pd_rd_wg=hbOLG&pd_rd_r=91da58c4-f349-4bfe-8f30-31ef6f81ffc6&pd_rd_i=B07L8512GK"  # Remplacez par l'URL de votre choix

print("Scraping des avis...")
reviews = scrape_amazon_reviews(url)

if reviews:
    print(f"{len(reviews)} avis récupérés.")
    insert_reviews(reviews)

    all_reviews = fetch_all_reviews()
    total_reviews = len(all_reviews)

    valid_ratings = [float(r[2].split()[0]) for r in all_reviews if r[2] and r[2] != "0"]

    if valid_ratings:
        average_rating = sum(valid_ratings) / len(valid_ratings)
        print(f"Nombre total d'avis : {total_reviews}")
        print(f"Note moyenne : {average_rating:.2f}")
        for review in all_reviews:
            print(f"Utilisateur : {review[4]}, Note : {review[2]}, Titre : {review[1]}, Commentaire : {review[3]}")
    else:
        print("Aucune note valide trouvée.")
else:
    print("Aucun avis trouvé.")
