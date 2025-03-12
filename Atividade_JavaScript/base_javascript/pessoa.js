class Pessoa {
    constructor (nome, idade){
        this.nome = nome;
        this.idade = idade;

    }
}


Pessoa.prototype.apresentar = function(){
    console.log(`Olá, meu nome é ${this.nome} e tenho ${this.idade} anos`);
};

const pessoa1 = new Pessoa('João', 25);
pessoa1.apresentar();

// class TestePessoa{
//     constructor(altura, peso){
//         this.peso = peso;
//         this.altura = altura;
//     }
// }

// TestePessoa.prototype.socar = function(forca){
//     console.log(`voce foi socado com ${forca} de força`)
// }


// const pessoaTeste = new TestePessoa(2, 10);
// pessoaTeste.socar(20)