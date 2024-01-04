#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a new number to a singly linked list
 * @head: Pointer to the head of the linked list
 * @number: number to be inserted into list
 *
 * Return: Address of the new node if inserted, otherwise NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *former = NULL;

	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	while (current != NULL && current->n < number)
	{
		former = current;
		current = current->next;
	}

	if (former == NULL)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		former->next = new_node;
		new_node->next = current;
	}

	return (new_node);
}
