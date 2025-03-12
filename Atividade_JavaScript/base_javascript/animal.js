class Animal{
    constructor(nome){
        this.nome = nome
    }
}

Animal.prototype.falar = function(){
    console.log(`${this.nome} faz um som`)
}


class Cachorro extends Animal{
    constructor(nome){
        super(nome);
    }
}


Cachorro.prototype.falar = function(){
    console.log(`${this.nome} late.`);
};

class Gato extends Animal{
    constructor(nome){
        super(nome)
    }
}

Gato.prototype.falar = function(){
    console.log(`${this.nome} Mia`)
}

class Cavalo extends Animal{
    constructor(nome){
        super(nome)
    }
}

Cavalo.prototype.falar = function(){
    console.log(`${this.nome} Relincha`)
}



const cachorro = new Cachorro("maya")
cachorro.falar();// Saida: Rex late

const gato = new Gato("nenem")
gato.falar()

const cavalo = new Cavalo("jorge")
cavalo.falar()

