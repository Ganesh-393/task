try (BufferedReader br = new BufferedReader(new FileReader("file.txt"))) {
    String line;
    while ((line = br.readLine()) != null)
        System.out.println(line);
} catch (IOException e) {
    e.printStackTrace();
}

