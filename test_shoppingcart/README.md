# Shopping cart

Tasks requested:
- Make the receipt print items in the order that they were added
- Add a 'Total' line to the receipt. This should be the full price we should charge the customer
- Be able to fetch product prices from an external source (json file, database ...)
- Be able to display the product prices in different currencies (not only Euro).
- Update the test suite to extend coverage and limit the number of tests which need changing when changes are introduced
- Any other changes which improve the reliability of this code in production

If you do not have enough information, make any assumptions you would like and note them down with TODO comments. Feel free to make comments that highlight completion of the tasks listed above.

Please budget 3 hours to complete, and your code should be production ready, clean and tested! Please ensure the code is version controlled also, and make sure to make several commits with sensile commit messages while working on this. When submitting please either:
- Provide a Github/GitLab/etc. link that we can view and clone your work; or
- Use git-bundle (https://git-scm.com/docs/git-bundle) to create a bundle file and send this to us.

==========================================================================================================

ASSUMPTIONS :

External Source files - JSON format.
1 euro = 1.09 dollars.
1 euro = 88 rupees.
Every Product that we are adding, There must be corresponding price data in product_prices.json.
The rate conversions are connected to real-time API to get updated rates for the currencies. 

To Do:

Handled Quantity as Non Integer Datatype.
Handled Empty Source files exception.
Handled No Source files Exist exception.
Handled Empty Cart Exception as there will be no need of calculation at that scenario.
Handled Accessing Invalid Item.
Implement delete operation.
Ignore the Unwanted files.
Handle the whole application in github by maintaining commit messages and version control.


Execution:

Test the application by executing main.py

python main.py       --->  Starting point of the application

You can test individual functions too  ---> I specified in comments.

The whole code is handled by Exception Handling and logging for Monitoring.