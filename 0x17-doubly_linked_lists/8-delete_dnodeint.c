#include "lists.h"

/**
 * delete_dnodeint_at_index - delete a node at a given position
 * @head: pointer to head pointer of double linked list
 * @index: index to delete node
 * Return: 1 if succeeded, or -1 if failed
 */

int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{

	unsigned int i = 0;
	dlistint_t *tmp, *tmp2;

	if (*head == NULL)
		return (-1);

	tmp = *head;

	if (index == 0)
	{
		*head = tmp->next;
		free(tmp);
		return (1);
	}

	while (i < (index - 1) && tmp != NULL)
	{
		tmp = tmp->next;
		i++;
	}

	if (i != (index - 1) || tmp->next == NULL)
		return (-1);

	tmp2 = tmp->next;
	tmp->next = (tmp->next)->next;
	free(tmp2);

	return (1);
}
