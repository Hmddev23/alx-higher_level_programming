#include "lists.h"

/**
  * check_cycle - checks if a linked list has a cycle in it.
  *
  * @list: pointer to the head of the linked list.
  *
  * Return: 1 if there is a cycle, 0 otherwise
  */

int check_cycle(listint_t *list)
{
	listint_t *slw = list, *fst = list;

	while (fst && slw && fst->next)
	{
		slw = slw->next;
		fst = fst->next->next;

		if (slw == fst)
			return (1);
	}

	return (0);
}
