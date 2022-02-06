int main(void)
{

    // Variables
    float change = 0.00;
    int coins = 0;

    do
    {
        // Getting the change to be given
        change = get_float("Owed: ");

    }
    while (change < 0);

    // Getting the change owed to cents
    int change_owed = round(change * 100);

    // Get the change
    while (change_owed > 0)
    {

        // Check if quaters can be given
        if (change_owed >= 25)
        {
            change_owed -= 25;
        }

        // Check if dimes can be given
        else if (change_owed >= 10)
        {
            change_owed -= 10;
        }

        // Check if nickles can be given
        else if (change_owed >= 5)
        {
            change_owed -= 5;
        }

        // Give change in pennies
        else
        {
            change_owed -= 1;
        }

        // Incrementing the coin count
        coins + 1; // coins += 1
    }

    // Print the number of coins required
    printf("%i\n", coins);
}