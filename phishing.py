import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests

def get_company_logo(organization):
    api_url = 'https://api.api-ninjas.com/v1/logo?name={}'.format(organization)
    headers = {'X-Api-Key': '+6NBUwiNX9hlLqrSIYyX0A==Bh8BK87i4iobt8nU'}

    try:
        response = requests.get(api_url, headers=headers)
        print("Statut de la réponse :", response.status_code)  # Débogage
        print("Contenu brut de la réponse :", response.text)  # Débogage

        if response.status_code == 200:
            company_data = response.json()
            print("Données JSON :", company_data)  # Débogage

            # Vérifiez si la liste contient un élément et s'il possède une clé "image"
            if company_data and "image" in company_data[0]:
                return company_data[0]["image"]  # Retournez le lien du logo
            else:
                print("Aucune image trouvée pour cette organisation.")
                return None
        else:
            print(f"Erreur {response.status_code} : {response.text}")
            return None
    except requests.RequestException as e:
        print(f"Erreur lors de la requête API : {e}")
        return None

def send_phishing_email(recipient_email, user_name, organization, logo_url):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'cyberizan@gmail.com'
    smtp_password = 'txzo zbvh owmf insp'

    now = datetime.datetime.now()
    date_accès = now.strftime("%d %B %Y")
    heure_accès = now.strftime("%Hh%M")


    # Si le logo est introuvable, utilisez un logo par défaut ou un logo générique
    if not logo_url:
        logo_url = 'https://www.example.com/default_logo.png'  # Remplacez ceci par un logo générique ou une URL par défaut

    msg = MIMEMultipart()
    msg['From'] = f"{organization} <{smtp_username}>"
    msg['To'] = recipient_email
    msg['Subject'] = f'Alerte Sécurité – Nouvel appareil détecté pour votre compte {organization}'

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
                padding: 20px;
            }}
            .container {{
                background-color: white;
                width: 450px;
                margin: auto;
                border-radius: 8px;
                border: 1px solid #ddd;
                padding: 20px;
                text-align: center;
            }}
            .logo {{
                margin-bottom: 10px;
                width: 50%;        
                max-width: 150px;  
                height: auto;      
                display: block;
                margin-left: auto;
                margin-right: auto; 
            }}
            .circle {{
                width: 40px;
                height: 40px;
                line-height: 40px;
                border-radius: 50%;
                background-color: #4285F4;
                color: white;
                font-weight: bold;
                margin: auto;
                font-size: 18px;
            }}
            .btn {{
                display: inline-block;
                background-color: #4285F4;
                color: white;
                padding: 12px 20px;
                margin-top: 20px;
                text-decoration: none;
                border-radius: 4px;
                font-weight: bold;
            }}
            .footer {{
                font-size: 12px;
                color: gray;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <!-- Logo personnalisé pour l'organisation -->
            <img src="{logo_url}" class="logo" alt="{organization}">
            <h2>Nouvelle connexion au compte</h2>
            <div class="circle">{user_name[0].upper()}</div>
            <p>{recipient_email}</p>
            <hr>
            <p>Nous avons détecté une nouvelle connexion à votre compte {organization}. 
            Si c'était vous, aucune action de votre part n'est requise. Dans le cas contraire, 
            nous vous aiderons à sécuriser votre compte.</p>
            <a href="http://127.0.0.1:5000/fake-warning?user={user_name}" class="btn">Changer votre mot de passe</a>
            <div class="footer">
                Vous pouvez aussi voir l'activité liée à la sécurité de votre compte ici <br>
                
            </div>
        </div>
        
         <p style="font-size: 11px; color: #999; text-align: center;">
            Cet e-mail vous a été envoyé pour vous informer de modifications importantes apportées à votre compte 
            et aux services {organization} que vous utilisez.<br>
            © 2025 {organization} Ireland Ltd., Gordon House, Barrow Street, Dublin 4, Ireland
        </p>
    </body>
    </html>
    """
    msg.attach(MIMEText(html_content, 'html'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(msg)
            print("E-mail envoyé avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'e-mail: {e}")
