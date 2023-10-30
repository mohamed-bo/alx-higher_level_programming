#include "lists.h"

/**
 * check_cycle - unction that finds the loop in a linked list.
 * @list: head of list
 * Return: 0 if there no cycle else return 1
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise, *hare;

	tortoise = list;
	hare = list;
	while (hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
			return (1);
	}
	return (0);
}
