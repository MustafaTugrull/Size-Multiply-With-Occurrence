def find_max(t, z):
    max_value = -1
    
    # Ana dize üzerindeki alt dizileri kontrol etme
    for i in range(len(t)):
        for j in range(i + 1, len(t) + 1):

            substring = t[i:j]
            
            # Alt dizenin, arama dizesinde kaç kez geçtiği sayar
            occurrences = z.count(substring)
            
            # En büyük değeri güncelle: Alt dizenin uzunluğu ile tekrar sayısının çarpımı ile karşılaştırma
            max_value = max(max_value, len(substring) * occurrences)
    
    # En fazla tekrar eden alt dize bilgisini döndürür.
    return max_value


if __name__ == '__main__':
    result = find_max("acldm1labcdhsnd", "shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa")
    print(result)