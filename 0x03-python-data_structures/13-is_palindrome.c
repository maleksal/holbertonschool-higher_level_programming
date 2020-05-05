#include "lists.h"

/**
 * is_palindrome - check if a singly linked list is a palindrom
 * @head: pointer to singly linked list
 * Return: 1 if palindrom, else 0
 */


listint_t *reverse_listint(listint_t **head);
size_t listint_len(const listint_t *h);

int is_palindrome(listint_t **head)
{
	listint_t *x1Ptr = *head;
	listint_t *x2Ptr = *head;

	listint_t *mid_list;
	listint_t *orign = *head;
	listint_t *lenPtr = *head;

	if (!head || *head == NULL)
		return (0);

	if (listint_len(lenPtr) <= 1)
		return (0);

	while (x1Ptr && x2Ptr->next)
	{
		x2Ptr = x2Ptr->next->next;

		if (!x2Ptr)
		{
			mid_list = x1Ptr->next;
			break;
		}

		if (x2Ptr->next == NULL)
		{
			mid_list = x1Ptr->next->next;
			break;
		}

		x1Ptr = x1Ptr->next;
	}

	x1Ptr->next = NULL;
	mid_list = reverse_listint(&mid_list);

	while (orign)
	{
		if (orign->n != mid_list->n)
			return (0);
		orign = orign->next;
		mid_list = mid_list->next;
	}
	return (1);
}


/**
  * reverse_listint - reverse a linked list
  * @head: pointer
  * Return: pointer
  */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *next_node;
	listint_t *follower;

	if (!head || *head == NULL)
		return (NULL);

	next_node = *head;

	/* set first_node to NULL */
	follower = next_node;
	next_node = next_node->next;
	follower->next = NULL;

	while (next_node != NULL)
	{
		follower = next_node;
		next_node = next_node->next;
		follower->next = *head;
		*head = follower;
	}
	*head = follower;
	return (*head);
}

/**
  * listint_len - get length of linked list
  * @h: pointer to a user defined data type
  * Return: int
  */

size_t listint_len(const listint_t *h)
{
	int len = 0;

	while (h != NULL)
	{
		h = h->next;
		len++;
	}
	return (len);
}
