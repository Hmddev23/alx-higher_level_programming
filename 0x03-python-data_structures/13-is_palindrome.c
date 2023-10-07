#include"lists.h"

int is_palindrome(listint_t **head);

/**
  * res_lists - Reverse a linked list in place.
  *
  * @head: Pointer to pointer to the head of the list.
  *
  * Return: Pointer to the new head of the reversed list.
  */

listint_t *res_lists(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	*head = prev;
	return (*head);
}

/**
  * is_palindrome - Check if a linked list is a palindrome.
  *
  * @head: Pointer to pointer to the head of the list.
  *
  * Return: 1 if palindrome, 0 otherwise.
  */

int is_palindrome(listint_t **head)
{
	listint_t *tmp, *rev, *mid;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}
	tmp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		tmp = tmp->next;

	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);

	tmp = tmp->next->next;
	rev = res_lists(&tmp);
	mid = rev;

	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
	res_lists(&mid);

	return (1);
}
