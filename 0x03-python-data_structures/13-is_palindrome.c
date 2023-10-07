#include "lists.h"

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
	listint_t *slow = *head;
	listint_t *fast = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	listint_t *second_half = slow->next;
	res_lists(&second_half);

	listint_t *first_half = *head;
	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
			return (0);
		first_half = first_half->next;
		second_half = second_half->next;
	}

	res_lists(&slow->next);

	return (1);
}
