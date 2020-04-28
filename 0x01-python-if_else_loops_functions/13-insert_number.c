#include "lists.h"

/**
 * insert_node - insert node where number is < node->next
 * @head: linked list
 * @number: int number to be inserted
 * Return: pointer to new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *pointer = *head;

	if (*head == NULL)
	{
		new_node = add_nodeint_end(head, number);
		return (new_node);
	}

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;

	if (number < pointer->n)
	{
		new_node->next = pointer;
		*head = new_node;
		return (new_node);
	}

	while (pointer->next)
	{
		if (number < pointer->next->n)
		{
			new_node->next = pointer->next;
			pointer->next = new_node;
			return (new_node);
		}
		pointer = pointer->next;
	}

	new_node = add_nodeint_end(head, number);
	return (new_node);
}
