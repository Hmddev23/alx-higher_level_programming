#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Python.h>
#include <floatobject.h>

/**
  * print_python_bytes - Print python bytes objects information.
  *
  * @p: Python object parameter.
  *
  * Return: Nothing.
  **/

void print_python_bytes(PyObject *p)
{
	size_t i, length, size;
	char *string;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");

	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("    [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	string = PyBytes_AsString(p);
	length = size > 10 ? 10 : size;

	printf("    size: %lu\n", size);
	printf("    trying string: %s\n", string);
	printf("    first %lu bytes: ", length);

	for (i = 0; i < length; i++)
	{
		printf("%02hhx%s", string[i], i + 1 < length ? " " : "");
	}
	printf("\n");
}

/**
  * print_python_float - Print python float.
  *
  * @p: Python float parameter.
  *
  * Return: Nothing.
  **/

void print_python_float(PyObject *p)
{
	double dbl;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float"))
	{
		printf("	[ERROR] Invalid Float Object\n");
		return;
	}
	dbl = ((PyFloatObject *)p)->ob_fval;
	printf("  value: %s\n",
	PyOS_double_to_string(dbl, 'r', 0, Py_DTSF_ADD_DOT_0, NULL));
}

/**
  * print_python_list - Print python lists information.
  *
  * @p: Python object parameter.
  *
  * Return: Nothing.
  **/

void print_python_list(PyObject *p)
{
	int i;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list"))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the python List = %lu\n", ((PyVarObject *)p)->ob_size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < ((PyVarObject *)p)->ob_size; i++)
	{
		printf("Element %d: %s\n", i,
			((PyListObject *)p)->ob_item[i]->ob_type->tp_name);

		if (!strcmp(((PyListObject *)p)->ob_item[i]->ob_type->tp_name, "bytes"))
			print_python_bytes(((PyListObject *)p)->ob_item[i]);
		else if (!strcmp(((PyListObject *)p)->ob_item[i]->ob_type->tp_name, "float"))
			print_python_float(((PyListObject *)p)->ob_item[i]);
	}
}
