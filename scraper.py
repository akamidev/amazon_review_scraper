from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def init_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    service = Service("C:/chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def scrape_amazon_reviews(url):
    driver = init_driver()
    driver.get(url)
    time.sleep(3)

    reviews = []
    try:
        wait = WebDriverWait(driver, 10)

        while True:
            # Extraire les avis de la page actuelle
            review_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@data-hook='review']")))

            for element in review_elements:
                try:
                    title = element.find_element(By.XPATH, ".//a[@data-hook='review-title']").text
                except:
                    title = "Titre non disponible"

                try:
                    rating_element = element.find_element(By.XPATH, ".//i[contains(@class, 'a-icon-star')]")
                    rating = rating_element.get_attribute("class")
                    rating = rating.split("a-star-")[-1].strip()
                except:
                    rating = "0"

                try:
                    comment = element.find_element(By.XPATH, ".//span[@data-hook='review-body']").text
                except:
                    comment = "Commentaire non disponible"

                try:
                    user = element.find_element(By.XPATH, ".//span[@class='a-profile-name']").text
                except:
                    user = "Utilisateur anonyme"

                reviews.append((title, rating, comment, user))

            # Vérifier si le bouton "Suivant" est présent
            try:
                next_button = driver.find_element(By.XPATH, "//li[@class='a-last']/a")
                next_button.click()
                time.sleep(3)  # Attendre le chargement de la nouvelle page
            except:
                print("Aucune page suivante trouvée, fin du scraping.")
                break
    except Exception as e:
        print(f"Erreur lors du scraping : {e}")
    finally:
        driver.quit()

    return reviews
