#include "lists.h"

/**
  * insert_node - Insert a new node into a sorted linked list.
  *
  * @head: Pointer to the linked list head.
  * @number: Value to be inserted into the new node.
  *
  * Return: Pointer to the new node or NULL if allocation fails.
  */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (node == NULL || node->n >= number)
	{
		new_node->next = node;
		*head = new_node;
		return (new_node);
	}

	while (node->next && node->next->n < number)
	{
		node = node->next;
	}

	new_node->next = node->next;
	node->next = new_node;

	return (new_node);
}
