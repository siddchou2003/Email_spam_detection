Project structure

Email_spam_detection/
│
├── index.html           # Frontend UI
├── spam_classifier.py   # Model training and prediction
├── model.pkl            # Trained model (generated after running the script)
├── vectorizer.pkl       # TF-IDF vectorizer
├── style.css            # Basic styling (if included)
└── README.md            # Project documentation

Run the Python classifier:
   python spam_classifier.py

(Optional) Use with XAMPP:
   1. Place the project in htdocs folder.
   2. Start Apache server from XAMPP.
   3. Open the index.html in your browser.
