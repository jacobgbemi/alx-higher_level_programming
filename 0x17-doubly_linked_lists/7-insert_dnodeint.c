#include "lists.h"

/**
 * insert_dnodeint_at_index - insert a new node at a given position
 * @head: pointer to head pointer of doubly linked list
 * @idx: index to insert new node
 * @n: new node's data
 * Return: address of new node, or NULL if failed
 */

dlistint_t *insert_dnodeint_at_index(dlistint_t **head, unsigned int idx,
		int n)
{

	unsigned int i = 0;
	dlistint_t *new_node, *tmp;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(dlistint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = n;

	if (idx == 0)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	tmp = *head;
	while (i < (idx - 1))
	{
		tmp = tmp->next;
		i++;

		if (tmp == NULL)
		{
			free(new_node);
			return (NULL);
		}
	}

	new_node->next = tmp->next;
	tmp->next = new_node;
	return (new_node);
}
