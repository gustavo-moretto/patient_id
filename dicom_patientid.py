import pydicom
import os

# antes de iniciar, criar pasta para salvar os novos arquivos

# selecionar pasta com arquivos dicom corrompidos
lista = os.listdir('C:\\Users\\Elekta\\Desktop\\celio')

#'\\\\RADION05\\Arquivos Compartilhados\\2. Imagens Externas\\roberto'
print(f'Número de arquivos: {len(lista)}')

# criar patientID em cada arquivo da pasta selecionada acima
for count, file in enumerate(lista):
    print(count)
    # selecionar pasta em que estão os arquivos a serem modificados
    dataset = pydicom.dcmread(f'C:\\Users\\Elekta\\Desktop\\celio\\{file}', force=True)
    # colocar o nome do paciente e o ID do paciente
    dataset.PatientName = "celio"
    dataset.PatientID = 'celio'
    # selecionar pasta em que os arquivos serão salvos (LEMBRAR DE CRIAR A PASTA ANTES)
    dataset.save_as(f'C:\\Users\\Elekta\\Desktop\\Imagens PatientID\\celio\\{file}')