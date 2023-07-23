# A entrada consiste em várias linhas, sendo a primeira linha um inteiro N (1 ≤ N ≤ 10^6), o número de candidatos. Cada uma das próximas N linhas contém o nome de um candidato (uma string com até 100 caracteres), um inteiro A (0 ≤ A ≤ 10^4), representando sua experiência profissional, um inteiro B (0 ≤ B ≤ 10^4), representando suas habilidades técnicas e um inteiro C (0 ≤ C ≤ 10^4), representando suas realizações acadêmicas.

def quicksort(array):
    if len(array) < 2:
        return array  # Base case: arrays with 0 or 1 element are already “sorted.”
    else:
        pivot = array[0]  # Recursive case
        # Sub-array of all the elements less than the pivot
        less = [i for i in array[1:] if i <= pivot]
        # Sub-array of all the elements greater than the pivot
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

while True:
  number_candidatos = int(input(""))
  if number_candidatos > 0:
    break  

nome = input("")
a, b, c = int(input(""))


print(quicksort([10, 5, 2, 3]))