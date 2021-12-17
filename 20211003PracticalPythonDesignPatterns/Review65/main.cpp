#include "algo.h"

int main()
{
    std::cout << "Hello world!" << std::endl;

    cy::otopic("permutation_heap");
    cy::algo_permutation_heap();
    cy::otopic("permutation_sort");
    cy::algo_permutation_sort();
    cy::otopic("structure_changer");
    cy::algo_structure_changer();
    cy::otopic("mover");
    cy::algo_mover();
    cy::otopic("value_midification");
    cy::algo_value_modifier();
    cy::otopic("set");
    cy::algo_set();
    cy::otopic("query_value");
    cy::algo_query_value();
    cy::otopic("query_property");
    cy::algo_query_property();
    cy::otopic("raw_memory");
    cy::algo_raw_memory();
    cy::otopic("secret_rune");
    cy::algo_secret_rune();
    cy::otopic("lone_island");
    cy::algo_lone_island();

    std::cout << "\n\npress any key to continue..";
    std::cin.get();

    return 0;
}
