// Task 1: Code a Person class
class person {
    constructor(nam='Tom',age=20,energy=100){
        this.nam = nam,
        this.age = age,
        this.energy = energy
    }
    sleep() {
        return energy+=10
    }
    doSomethingFun() {
        return energy-=10
    }
}
// Task 2: Code a Worker class
class worker extends person{
    constructor(xp=0,hourlywage=10){
        this.xp=xp
        this.hourlywage=hourlywage
        super(nam,age,energy,sleep(),doSomethingFun())
    }
    gotowork() {
        return xp+=10
    }
}
// Task 3: Code an intern object, run methods
function intern() {
    let gulam=worker(name= 'Bob',age= 21,energy= 110,xp= 0,hourlyWage= 10)
    return gulam.gotowork()
}

// Task 4: Code a manager object, methods
function manager() {
    let manage=worker(name= 'Alice',age= 30,energy= 120,xp= 100,hourlyWage= 30)
    return manage.doSomethingFun()
}
console.log(intern())