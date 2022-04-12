#include "main.h"

/**
 * print_sign - prints the sign of a number n
 * @n: function parameter of type int
 * Return: returns 1 and prints + if n is grater thatn zero,
 */

int print_sign(int n)
{
	int value;

	if (n > 0)
	{
		value =1;
		_putchar('+');
	}
	else if (n == 0)
	{
		value = 0;
		_putchar('0');
	}
	else
	{
		value = -1;
		_putchar('-');
	}
	return (value);
}
