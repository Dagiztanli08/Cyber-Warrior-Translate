# c-eviri-2
Önceden kodlamış olduğum çeviri programına yeni özellikler eklendi.

Programımızın çalışma mantığı;

Öncelikle bilgisayarın kopyalama hafızanı dinler ve kopyalanan değeri google api sayesinde ingilizce'ye çevrir çevirdikten sonra,
databaseye ekler ve birdaha aynı kelimeyi kopyaladığınızda internet harcamadan databaseden bu veriyi çeker.
eğer databasede yoksa bu kelime api kullanarak databaseye ekler.
