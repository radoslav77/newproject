
let counarr = []
let coun = 0
let counM = 0
let counL = 0
let counR = 0
let desC = 0  
let desB = 0
let desM = 0
let desM8 = 0
let desMaamul = 0
let desArab = 0 
let drkWater = 0 
let drkN = 0 
let drkWW = 0
let drkCh = 0
let drkRW = 0
    const amenitiesEl = document.getElementsByClassName('amenities')
    const TomorrowDate = document.getElementById('date')

   // need to import jason and compare arrival name with amenities 
   // and input it back to page as combined + total  
   var FruitAmenitie = ['Large fruit','Midium fruit','Small fruit','Presidential'] 

    let arr = []
    for (let item of amenitiesEl) {
    //console.log(item.innerText)
    let nArr = item.innerText.split(',')
        arr.push(nArr)
    }
    
    arr.forEach(el => {

      el.forEach(element => {
        if(FruitAmenitie.includes(element)){
           //console.log(element)
        }
      })

        //console.log(el)
    })
    
    const JSON_data = ('/json_data')
    GetData(JSON_data)
    async function GetData(url) {
        const res = await fetch(url)
        const data = await res.json()
 
 
        //console.log(data)

function size_dict(d){c=0; for (i in d) ++c; return c}  

let numCount = {key: {type:'none',
                       num: 0},
                des: {Dtype: 'none',
                      Dnum: 0},
                drk: {drktype: 'none',
                    drknum: 0}
                }

let size = size_dict(numCount)



        data.forEach(e => {
            
            //var date = new Date().toLocaleDateString()
            //var currentDate = date.getFullYear() + '-' + date.getrMonth() + '-' + date.getDate()
            
            /*
            //getting date of today and adding one day to it
            var today = new Date()
            var tomorrow = new Date()
            tomorrow.setDate(today.getDate()+1)
            console.log(tomorrow)*/

            //console.log(TomorrowDate.innerText)
            //console.log(e.date,' ',e.arrival_date)
            //console.log(e)
            if (e.arrival_date === TomorrowDate.innerText){
                //console.log(e.name, '+', e.fruit_amenity, '+', e.arrival_date )
                

                numCount.key.type = e.fruit_amenity
                numCount.key.num= e.num_fruit
                numCount.des.Dtype = e.dessert_amenity
                numCount.des.Dnum = e.num_dessrt
                numCount.drk.drktype = e.drink_amenity
                numCount.drk.drknum = e.num_drink
                //numCount.num = e.num_fruit
                
                //console.log(size)
                for(var key in numCount){
                    //console.log(key+ ':' + numCount[key])
                    if ( e.fruit_amenity == 'Small fruit'){
                        //var Ccoun = 0
                        coun =  (coun + numCount.key.num) 

                    } else if (e.fruit_amenity == 'Midium fruit'){
                        counM = counM + numCount.key.num

                    }else if (e.fruit_amenity == 'Large fruit'){
                        counL = counL + numCount.key.num

                    }else if (e.fruit_amenity == 'Presidential')
                        ounR = counR + numCount.key.num
                }
               
                for (var key in numCount){
                     if (e.dessert_amenity == 'Chocolate truffle'){
                        desC = desC + numCount.des.Dnum
                        
                    }else if(e.dessert_amenity == 'Baklava'){
                        
                        desB = desB + numCount.des.Dnum
                        
                    }else if(e.dessert_amenity == 'Macaroons 4pcs'){
                       
                        desM = desM + numCount.des.Dnum
                    }else if (e.dessert_amenity == 'Macaroons 8pcs'){
                        desM8 = desM8 + numCount.des.Dnum
                    }else if (e.dessert_amenity == 'Maamul'){
                        desMaamul = desMaamul + numCount.des.Dnum
                    }else if ( e.dessert_amenity == 'Arab amenity'){
                        desArab = desArab + numCount.des.Dnum
                    }
                     //console.log(e.dessert_amenity, '-', numCount.des)
                }
                 
                for (var key in numCount){
                    
                    if (e.drink_amenity == 'Water'){
                        
                        drkWater = drkWater + numCount.drk.drknum
                        console.log(drkWater)
                    }else if(e.drink_amenity == 'Negroni'){
                        drkN = drkN + numCount.drk.drknum
                    }else if (e.drink_amenity == 'White wine'){
                        drkWW = drkWW + numCount.drk.drknum
                    }else if (e.drink_amenity == 'Champagne'){
                        drkCh = drkCh + numCount.drk.drknum
                    }else if (e.drink_amenity == 'Red wine'){
                        drkRW = drkRW + numCount.drk.drknum
                    }
                }



                //console.log(numCount)
            }
            
        });

            let newS = coun / coun.length 

                const ulEl = document.getElementById('total')
                console.log(coun)
                var liEl = document.createElement('li')
                liEl.innerHTML = `<div id="total_taly">
                                        <div id="taly">
                                        <p>Small Fruit total : ${ coun / size }</p>
                                        <p>Midium Fruit total : ${counM / size  }</p>
                                        <p>Large Fruit total : ${counL / size  }</p>
                                        <p>Chocolaet traffles : ${desC / size  }</p>
                                        <p>Baklava total : ${desB / size  }</p>
                                        <p>Macaroons 4pcs total: ${desM / size  }</p>
                                        <p>Water total: ${drkWater / size  }</p>
                                        <p>Negroni total: ${drkN / size  }</p>
                                        <p>White Wine total: ${drkWW / size  }</p>
                                        <p>Champadne total: ${drkCh / size  }</p>
                                        <p>Red Wine total: ${drkRW / size  }</p>
                                        </div>
                                    </div>`
                
                                  
                ulEl.appendChild(liEl)



    }


        //console.log(coun, '-', counM,' ', counL)
    const LiElments = document.getElementById('total')
    for(let i = 0; i < LiElments.length; i++){
        console.log(LiElments[i])
        if( LiElments[i].innerHTML == 'undefined'){
            LiElments[i].style.display = 'none'
        }else if (LiElments[i].innerText == 0){
            LiElments[i].style.display = 'none'
        }
    }


