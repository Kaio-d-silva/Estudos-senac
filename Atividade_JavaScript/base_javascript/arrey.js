Array.prototype.ultimo = function(){
    return this[this.length - 1]
}

const numeros = [1,2,3,4]
console.log(numeros.ultimo());


Array.prototype.primeiro = function(){
    return this[0]
}


const frutas = ["maça", "pera", "cupuasul"]
console.log(frutas.primeiro())

