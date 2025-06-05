from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/fake-warning')
def fake_warning():
    user = request.args.get('user', 'utilisateur inconnu')
    html = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Simulation de phishing</title>
        <style>
            body {{
                background-color: #fff3cd;
                font-family: Arial, sans-serif;
                padding: 40px;
                text-align: center;
            }}
            .box {{
                background-color: #fff;
                border: 2px solid #ffeeba;
                border-radius: 10px;
                padding: 30px;
                max-width: 600px;
                margin: auto;
            }}
            h1 {{
                color: #856404;
            }}
            p {{
                color: #856404;
                font-size: 18px;
            }}
        </style>
    </head>
    <body>
        <div class="box">
            <h1>⚠️ Simulation de Phishing</h1>
            <p>Bonjour <strong>{user}</strong>,</p>
            <p>Vous avez cliqué sur un lien simulant une attaque de hameçonnage (phishing).</p>
            <p>Ce test est réalisé dans un cadre pédagogique pour sensibiliser aux risques de cybersécurité.</p>
            <p><strong>Aucune information sensible n'a été collectée.</strong></p>
            <p>Restez vigilant face aux courriels suspects et vérifiez toujours l'origine d'un lien avant de cliquer !</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(port=5000)
