#include "lists.h"


/**
 * check_cycle - checks if a singly linked list has a cycle in it,
 * using Floyd's cycle detection algorithm.
 *
 * @list: points to singly linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{

	listint_t *pt = list;
	listint_t *pt_x2 = list;

	if (!list)
		return (0);

	while (pt && pt_x2 && pt_x2->next)
	{
		pt = pt->next;
		pt_x2 = pt_x2->next->next; /* move by 2*/

		if (pt == pt_x2)
			return (1);
	}

	return (0);
}
