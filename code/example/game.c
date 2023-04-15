#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#define NUM_OF_ITEMS 10

struct userInfo 
{
	int user_id;
	int balance;
	int items[NUM_OF_ITEMS];
	int count;
};

struct userInfo user;
int items[NUM_OF_ITEMS];

__attribute__((noreturn, noinline)) void report_error()
{
    while (1)
        ;
}

void Buy(int price, int item) 
{
			DecreaseBalance(price);
	IncreaseItem(item);
}
bool CanBuy(int balance, int price) 
{
	return balance >= price && price > 0;
}

void DecreaseBalance(int price) 
{
	user.balance -= price;
}

void IncreaseItem(int item) 
{
	user.items[item] += 1;
	user.count += 1;
}

void BuyItem (int item_id)
{
	int price = items[item_id];
	int balance = user.balance;
	
	bool canBuy = CanBuy(balance, price);
	if (!canBuy)
	{
		report_error();
		return;
	}

	Buy(price, item_id);
}

void init_user()
{
	user.user_id = 1;
	user.balance = 10;
	for (int i = 0; i < NUM_OF_ITEMS; i++)
	{
		user.items[i] = 0;
	}
	user.count = 0;
}
void init_items()
{
	for (int i = 0; i < NUM_OF_ITEMS; i++)
	{
		items[i] = (i + 11) * (i + 4);
	}

}

int Tbmain()  
{
	init_user();
	init_items();

	int item = 3;
	BuyItem(item);
}
