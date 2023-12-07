#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info -  function that prints some basic
 *@PyObject info about Python lists
 * @p: python list
 */
void print_python_list_info(PyObject *p)
{
	int ment;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (ment = 0; ment < Py_SIZE(p); ment++)
		printf("Element %d: %s\n", ment, Py_TYPE(PyList_GetItem(p, ment))->tp_name);
}
