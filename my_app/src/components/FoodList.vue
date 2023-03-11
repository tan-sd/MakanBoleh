<template>
    <div class="accordion accordion-flush" id="food_accordian">

        <!-- V-FOR STARTS HERE -->
        <div class="accordion-item" v-for="(e_buff, index) in buffets" :key="index">
            <h2 class="accordion-header" :id="`flush-heading${index}`">

            <!-- HEADER GOES HERE v -->
            <button class="accordion-button collapsed bg-light" type="button" data-bs-toggle="collapse" :data-bs-target="`#flush-collapse${index}`" aria-expanded="false" :aria-controls="`flush-collapse${index}`" @click="focus_on_buffet(index)">
                <div class="row vw-100">
                    <div class="col-5">
                        <img :src="require(`../assets/images/buffet_imgs/buffet${index%3+1}.jpg`)" class="img-fluid">
                    </div>
                    <div class="col-7">
                        <div class="row">
                            <div class="col-12 col-md-3">
                                <h6><font-awesome-icon icon="fa-solid fa-location-dot" /> {{ e_buff.location.slice(0,20) }}</h6>
                            </div>
                            <div class="col-12 col-md-3">
                                <h6>
                                    <i v-for="(e_diet, index) in e_buff.diet_res" :key="index">
                                        <font-awesome-icon :icon="diet_icons[e_diet]" />&nbsp;
                                    </i>
                                </h6>
                            </div>
                            <div class="col-12 col-md-3">
                                <h6><font-awesome-icon icon="fa-solid fa-hourglass-half" /> {{ e_buff.time_left }} </h6>
                            </div>
                        </div>
                    </div>
                </div>
            </button>

            </h2>
            <div :id="`flush-collapse${index}`" class="accordion-collapse collapse" :aria-labelledby="`flush-heading${index}`" data-bs-parent="#food_accordian">
            
            <!-- BODY GOES HERE v -->
            <div class="accordion-body bg-dark text-white">
                {{ e_buff.description }}
                <button class="btn btn-main">Click here to route</button>
            </div>
            </div>
        </div>
    </div>
</template>


<script>
    export default{
        props: [],

        data() {
            return{
                buffets: [
                    {
                        description: 'Food at SOL',
                        location: '1 Joo Koon Cir, #13-01 FairPrice Hub, Singapore 629117',
                        distance: '5km',
                        end_time: '2023-03-11T11:15:00',     // yyyy-mm-ddThh:mm:ss <- T is only a seperator
                        diet_res: ['halal', 'vegetarian', 'nobeef'],
                        time_left: '',
                    },

                    {
                        description: 'Food at Esplanade. Really delicious, got chicken wings, burger, nuggets, bull penis, ice cream and chocolate cake! Come fast cos confirm very fast clear one~ :)Food at Esplanade. Really delicious, got chicken wings, burger, nuggets, bull penis, ice cream and chocolate cake! Come fast cos confirm very fast clear one~ :)Food at Esplanade. Really delicious, got chicken wings, burger, nuggets, bull penis, ice cream and chocolate cake! Come fast cos confirm very fast clear one~ :)',
                        location: '1 Esplanade Dr, Singapore 038981',
                        distance: '1km',
                        end_time: '2023-03-11T22:00:00',
                        diet_res: ['halal'],
                        time_left: '',
                    },

                    {
                        description: 'Food at ur mom\'s house',
                        location: '65 Chulia St, OCBC Centre, Singapore 049513',
                        distance: '69km',
                        end_time: '2023-03-11T22:30:00',
                        diet_res: ['vegetarian'],
                        time_left: '',
                    },

                    {
                        description: 'Food at SOL',
                        location: 'SOL',
                        distance: '5km',
                        end_time: '2023-03-11T21:30:00',     // yyyy-mm-ddThh:mm:ss <- T is only a seperator
                        diet_res: ['halal', 'vegetarian'],
                        time_left: '',
                    },

                    {
                        description: 'Food at Esplanade. Really delicious, got chicken wings, burger, nuggets, bull penis, ice cream and chocolate cake! Come fast cos confirm very fast clear one~ :)',
                        location: 'Esplanade',
                        distance: '1km',
                        end_time: '2023-03-11T22:00:00',
                        diet_res: [],
                        time_left: '',
                    },

                    {
                        description: 'Food at ur mom\'s house',
                        location: 'You mom\'s house',
                        distance: '69km',
                        end_time: '2023-03-11T22:30:00',
                        diet_res: ['vegetarian'],
                        time_left: '',
                    }
                ],

                diet_icons: {
                    'halal': 'fa-solid fa-star-and-crescent',
                    'vegetarian': 'fa-solid fa-leaf',
                    'nobeef': 'fa-solid fa-cow'
                },
            }
        },

        methods: {
            get_time_left() {
                let curr_time = new Date();

                for (let e_buff of this.buffets) {
                    let end_time = new Date(e_buff.end_time);
    
                    let hr_left = Math.floor( (Math.max(end_time-curr_time, 0)) / 1000 / 60 / 60 );
                    let min_left = Math.floor( (Math.max(end_time-curr_time, 0)) / 1000 / 60 % 60 );
                    let sec_left = Math.floor( (Math.max(end_time-curr_time, 0)) / 1000 % 60 );

                    e_buff.time_left = `${hr_left}hr ${min_left}min ${sec_left}s`;
                }

                setTimeout(this.get_time_left, 1000)
            },

            current_expanded() {
                console.log(`=== [START] expanded() ===`)
                
                let accordian_elem = document.getElementById("food_accordian")

                if (accordian_elem == null) {return -1}

                let accordian_children = accordian_elem.children

                let e_idx = -1

                for (let e_child of accordian_children) {
                    e_idx += 1

                    let is_expanded = e_child.querySelector(`[aria-expanded='true']`)
                    
                    if (is_expanded) {
                        return e_idx
                    }
                }

                return -1
            },

            focus_on_buffet(idx) {
                console.log(`=== [START] focus_on_buffet(${idx}) ===`)
                
                if (idx == -1) { idx = 0 }

                let focus_elem = document.getElementById(`flush-heading${idx}`)

                setTimeout(() => {
                    focus_elem.scrollIntoView({ behavior: 'smooth'})
                }, "300")

                console.log(`=== [END] focus_on_buffet(${idx}) ===`)
                return
            }
        },

        computed: {
        },

        created() {
            this.get_time_left()
        }
    }
</script>


<style scoped>
    #food_accordian{
        position: fixed;
        bottom: 0;
        right: 0;
        left: 0;
        overflow: scroll;
        max-height: 40vh;
        transition: all .8s ease-in-out;
        border-radius: 12px 12px 0px 0px;
    }

    #food_accordian:has(.accordion-button[aria-expanded='true']) {
        max-height: 60vh;
    }
</style>