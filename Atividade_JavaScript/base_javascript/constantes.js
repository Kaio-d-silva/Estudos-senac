function Config(servidor, porta){
    this.servidor = servidor;
    this.porta = porta;
}

Config.prototype.mostrarConfig = function(){
    console.log(`Servidor :${this.servidor} Porta:${this.porta}`);
}

const config1 = new Config("localhost", 8080);
config1.mostrarConfig();