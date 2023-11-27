#include &quot;lists.h&quot
/**
* check_cycle - function checks if a singly linked list has a cycle in it.
* @list: pointer to the beginning of the node
* Return: 0 if no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *current, *check;
	if (list == NULL || list-&gt;next == NULL)
		return (0);
	current = list;
	check = current-&gt;next;
	while (current != NULL &amp;&amp; check-&gt;next != NULL
			&amp;&amp; check-&gt;next-&gt;next != NULL)
	{
		if (current == check)
			return (1);
		current = current-&gt;next;
		check = check-&gt;next-&gt;next;
	}
	return (0);
}
