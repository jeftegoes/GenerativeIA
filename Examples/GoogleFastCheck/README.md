1. Create a Google Cloud Project
   Go to the Google Cloud Console.
   Click the project dropdown at the top and select New Project.
   Enter a name for your project and click Create.
   Google for Developers
   Google for Developers
   +4
2. Enable the Fact Check Tools API
   Navigate to the API Library in the Cloud Console.
   Search for "Fact Check Tools API" and select it.
   Click Enable to activate the service for your project.
   Google for Developers
   Google for Developers
   +2
3. Generate the API Key
   Go to the APIs & Services > Credentials page.
   Click + Create Credentials at the top of the page.
   Select API key from the dropdown menu.
   A dialog will appear with your new API key string. Copy and save this key securely.
   Google Help
   Google Help
   +4
4. Important Restrictions & Use Cases
   Security: It is highly recommended to click Edit API key immediately after creation to restrict it to only the "Fact Check Tools API" to prevent unauthorized usage.
   Querying Data: Once you have the key, you can perform Claim Searches by sending an HTTP GET request to:
   https://googleapis.com{TEXT}&key={YOUR_API_KEY}.
   Writing Markup: To use the ClaimReview Markup API (to submit fact-checks), your site must first be verified in Google Search Console.

# URL base

- https://factchecktools.googleapis.com/v1alpha1/claims:search?query=urna%20fraudada&languageCode=pt-BR&key=AIzaSyDA_5wsZ0SwsoRqMZ-GuAitQZK-ZZSHgnM
