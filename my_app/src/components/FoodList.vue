<template>
    <div class="accordion accordion-flush text-extra-dark bg-extra-light" id="food_accordian">
        <!-- HEADER W BUTTONS -->
        <div class="accordion-item bg-dark text-light py-3 m-0 row" v-if="my_buffets.length > 0">
            <div class="col-6 d-flex justify-content-center">
                <button class="btn" :class="{'fw-bold btn-main-secondary-fixed': to_display == 'mine', 'btn-main-light-fixed': to_display != 'mine'}" @click="to_display = 'mine' ">My Buffets</button>
            </div>

            <div class="col-6 d-flex justify-content-center">
                <button class="btn" :class="{'fw-bold btn-main-secondary-fixed': to_display == 'other', 'btn-main-light-fixed': to_display != 'other'}" @click="to_display = 'other' ">Other Buffets</button>
            </div>
        </div>

        <!-- MY BUFFETS -->
        <div v-if="to_display == 'mine' ">
            <!-- V-FOR MY_BUFFETS STARTS HERE -->
            <div class="accordion-item" v-for="(e_buff, index) in my_buffets" :key="index" >
                <h2 class="accordion-header" :id="`mybuff-flush-heading${index}`">
    
                <!-- HEADER GOES HERE v -->
                <button class="accordion-button collapsed bg-light" type="button" data-bs-toggle="collapse" :data-bs-target="`#mybuff-flush-collapse${index}`" aria-expanded="false" :aria-controls="`mybuff-flush-collapse${index}`" @click="focus_on_buffet(index, true)">
                    <div class="row vw-100">
                        <!-- IMAGE -->
                        <div class="col-5 col-md-4 col-lg-5">
                            <img :src="require(`../assets/images/buffet_imgs/buffet${index%3+1}.jpg`)" class="img-fluid">
                        </div>

                        <!-- DETAILS -->
                        <div class="col-7 col-md-8 col-lg-7">
                            <div class="row">
                                <!-- DIET RESTRICTIONS -->
                                <div class="col-12 col-md-3">
                                    <h6>
                                        <i v-for="(e_diet, index) in e_buff.diet_res" :key="index">
                                            <font-awesome-icon :icon="diet_icons[e_diet]" />&nbsp;
                                        </i>
                                    </h6>
                                </div>

                                <!-- TIME LEFT -->
                                <div class="col-12 col-md-3">
                                    <h6><font-awesome-icon icon="fa-solid fa-hourglass-half" /> {{ e_buff.time_left }} </h6>
                                </div>
                            </div>
                        </div>
                    </div>
                </button>
    
                </h2>
                <div :id="`mybuff-flush-collapse${index}`" class="accordion-collapse collapse" :aria-labelledby="`flush-heading${index}`" data-bs-parent="#food_accordian">
                
                <!-- BODY GOES HERE v -->
                <div class="accordion-body bg-light-gradient">
                    <div class="container-fluid">
                        <div class="row">
                            <div class="col-12 col-lg-8">
                                <h6>
                                    <font-awesome-icon icon="fa-solid fa-location-dot" /> {{ e_buff.location }}
                                </h6>

                                <p>
                                    {{ e_buff.description }}
                                </p>
                            </div>
                            <div class="col-12 col-lg-4 d-flex justify-content-center align-items-center">
                                <div>
                                    <button class="btn btn-warning">
                                        <font-awesome-icon icon="fa-solid fa-circle-stop" />&nbsp;&nbsp;End Buffet
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                        
                </div>
                </div>
            </div>        
        </div>

        <!-- OTHER BUFFETS -->
        <div v-if="to_display == 'other' ">
            <!-- V-FOR BUFFETS STARTS HERE -->
            <div class="accordion-item" v-for="(e_buff, index) in buffets" :key="index" >
                <h2 class="accordion-header" :id="`flush-heading${index}`">
    
                <!-- HEADER GOES HERE v -->
                <button class="accordion-button collapsed bg-light" type="button" data-bs-toggle="collapse" :data-bs-target="`#flush-collapse${index}`" aria-expanded="false" :aria-controls="`flush-collapse${index}`" @click="focus_on_buffet(index, false)">
                    <div class="row vw-100">
                        <!-- IMAGE -->
                        <div class="col-5 col-md-4 col-lg-5">
                            <img :src="require(`../assets/images/buffet_imgs/buffet${index%3+1}.jpg`)" class="img-fluid">
                        </div>

                        <!-- DETAILS -->
                        <div class="col-7 col-md-8 col-lg-7">
                            <div class="row">
                                <!-- DIET RESTRICTIONS -->
                                <div class="col-12 col-sm-6 col-md-3">
                                    <h6>
                                        <i v-for="(e_diet, index) in e_buff.diet_res" :key="index">
                                            <font-awesome-icon :icon="diet_icons[e_diet]" />&nbsp;
                                        </i>
                                    </h6>
                                </div>

                                <!-- TIME LEFT -->
                                <div class="col-12 col-sm-6 col-md-3">
                                    <h6><font-awesome-icon icon="fa-solid fa-hourglass-half" /> {{ e_buff.time_left }} </h6>
                                </div>

                                <!-- DISTANCE -->
                                <div class="col-12 col-sm-6 col-md-3" v-if="user_lat">
                                    <h6><font-awesome-icon icon="fa-solid fa-person-walking" /> {{ e_buff.distance }}</h6>
                                </div>
                            </div>
                        </div>
                    </div>
                </button>
    
                </h2>
                <div :id="`flush-collapse${index}`" class="accordion-collapse collapse" :aria-labelledby="`flush-heading${index}`" data-bs-parent="#food_accordian">
                
                <!-- BODY GOES HERE v -->
                <div class="accordion-body bg-light-gradient">
                    <div class="container-fluid">
                        <div class="row">
                            <div class="col-12 col-lg-8">
                                <h6>
                                    <font-awesome-icon icon="fa-solid fa-location-dot" /> {{ e_buff.location }}
                                </h6>

                                <p>
                                    {{ e_buff.description }}
                                </p>
                            </div>
                            <div class="col-12 col-lg-4 d-flex justify-content-center align-items-center">
                                <div>
                                    <button class="btn btn-main">
                                        <font-awesome-icon icon="fa-solid fa-circle-arrow-right" />&nbsp;&nbsp;Route to Buffet
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                        
                </div>
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
                        lat: 1.3267935951952476,
                        long: 103.67878198117971,
                        distance: null,
                        end_time: '2023-03-12T11:15:00',     // yyyy-mm-ddThh:mm:ss <- T is only a seperator
                        diet_res: ['halal', 'vegetarian', 'nobeef'],
                        time_left: '',
                    },

                    {
                        description: 'Food at Esplanade. Really delicious, got chicken wings, burger, nuggets, bull penis, ice cream and chocolate cake! Come fast cos confirm very fast clear one~ :)Food at Esplanade. Really delicious, got chicken wings, burger, nuggets, bull penis, ice cream and chocolate cake! Come fast cos confirm very fast clear one~ :)Food at Esplanade. Really delicious, got chicken wings, burger, nuggets, bull penis, ice cream and chocolate cake! Come fast cos confirm very fast clear one~ :)',
                        location: '1 Esplanade Dr, Singapore 038981',
                        lat: 1.2898355468246039,
                        long: 103.85527989652236,
                        distance: null,
                        end_time: '2023-03-12T22:00:00',
                        diet_res: ['halal'],
                        time_left: '',
                    },

                    {
                        description: 'Food at ur mom\'s house',
                        location: '17 Petir Rd, Singapore 678278',
                        lat: 1.3784975491700686,
                        long: 103.76300728853624,
                        distance: null,
                        end_time: '2023-03-12T22:30:00',
                        diet_res: ['vegetarian'],
                        time_left: '',
                    },
                ],

                my_buffets: [
                    {
                        description: 'My Buffet 1',
                        location: '1 Joo Koon Cir, #13-01 FairPrice Hub, Singapore 629117',
                        lat: 1.3267935951952476,
                        long: 103.67878198117971,
                        end_time: '2023-03-12T11:15:00',     // yyyy-mm-ddThh:mm:ss <- T is only a seperator
                        diet_res: ['halal', 'vegetarian', 'nobeef'],
                        time_left: '',
                    },

                    {
                        description: 'My Buffet 2',
                        location: '1 Esplanade Dr, Singapore 038981',
                        lat: 1.2898355468246039,
                        long: 103.85527989652236,
                        end_time: '2023-03-12T22:00:00',
                        diet_res: ['halal'],
                        time_left: '',
                    },
                ],

                diet_icons: {
                    'halal': 'fa-solid fa-star-and-crescent',
                    'vegetarian': 'fa-solid fa-leaf',
                    'nobeef': 'fa-solid fa-cow'
                },

                curr_focused: 0,

                user_lat: null,
                user_long: null,

                to_display: 'other',
            }
        },

        methods: {
            update_buffet_time_left() {
                let curr_time = new Date();

                for (let e_buff of this.buffets) {
                    // UPDATES TIME_LEFT
                    let end_time = new Date(e_buff.end_time);
    
                    let hr_left = Math.floor( (Math.max(end_time-curr_time, 0)) / 1000 / 60 / 60 );
                    let min_left = Math.floor( (Math.max(end_time-curr_time, 0)) / 1000 / 60 % 60 );
                    let sec_left = Math.floor( (Math.max(end_time-curr_time, 0)) / 1000 % 60 );

                    e_buff.time_left = `${hr_left}hr ${min_left}min ${sec_left}s`;
                }

                for (let e_buff of this.my_buffets) {
                    // UPDATES TIME_LEFT
                    let end_time = new Date(e_buff.end_time);
    
                    let hr_left = Math.floor( (Math.max(end_time-curr_time, 0)) / 1000 / 60 / 60 );
                    let min_left = Math.floor( (Math.max(end_time-curr_time, 0)) / 1000 / 60 % 60 );
                    let sec_left = Math.floor( (Math.max(end_time-curr_time, 0)) / 1000 % 60 );

                    e_buff.time_left = `${hr_left}hr ${min_left}min ${sec_left}s`;
                }

                setTimeout(this.update_buffet_time_left, 1000)
            },

            update_buffet_distance() {
                console.log(`=== [START] update_buffet_distance() ===`)
                
                for (let e_buff of this.buffets) {
                    // UPDATES DISTANCE
                    let target_lat = e_buff.lat
                    let target_long = e_buff.long
                    let distance_km = this.get_distance_km(target_lat, target_long, this.user_lat, this.user_long)

                    console.log("User curr latlong", this.user_lat, this.user_long)

                    if (distance_km >= 1) {
                        e_buff.distance = distance_km.toFixed(1).toString() + "km"
                    } else {
                        e_buff.distance = Math.round(distance_km * 1000).toString() + 'm'
                    }
                }

                console.log(`=== [END] update_buffet_distance() ===`)
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

            focus_on_buffet(idx, is_my_buff) {
                console.log(`=== [START] focus_on_buffet(${idx}) ===`)
                let prefix = ''

                if (is_my_buff) {
                    prefix = 'mybuff-'
                }
                
                if (idx == -1) { idx = 0 }

                let focus_elem = document.getElementById(`${prefix}flush-heading${idx}`)

                setTimeout(() => {
                    focus_elem.scrollIntoView({ behavior: 'smooth'})
                }, "300")

                console.log(`=== [END] focus_on_buffet(${idx}) ===`)
                return
            },

            update_user_latlong(position) {
                console.log(`=== [START] update_user_latlong() ===`)
                
                this.user_lat = position.coords.latitude
                this.user_long =  position.coords.longitude

                this.update_buffet_distance()

                console.log(`=== [END] update_user_latlong() ===`)
            },

            getLocation() {
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(this.update_user_latlong);
                }
            },

            get_distance_km(lat1, lon1, lat2, lon2) {
                var R = 6371; // Radius of the earth in km
                var dLat = this.deg2rad(lat2-lat1);  // deg2rad below
                var dLon = this.deg2rad(lon2-lon1); 
                var a = 
                    Math.sin(dLat/2) * Math.sin(dLat/2) +
                    Math.cos(this.deg2rad(lat1)) * Math.cos(this.deg2rad(lat2)) * 
                    Math.sin(dLon/2) * Math.sin(dLon/2)
                    ; 
                var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a)); 
                var d = R * c; // Distance in km
                return d;
            },

            deg2rad(deg) {
                return deg * (Math.PI/180)
            },
        },

        computed: {
        },

        async created() {
            this.getLocation()
            this.update_buffet_time_left()
        }
    }
</script>


<style scoped>
    /* Up to LG */
    @media (max-width: 769px) {
        #food_accordian{
            position: fixed;
            bottom: 0;
            right: 0;
            left: 0;
            overflow-y: scroll;
            max-height: 40vh;
            transition: all .8s ease-in-out;
            border-radius: 12px 12px 0px 0px;
        }

        #food_accordian:has(.accordion-button[aria-expanded='true']) {
            max-height: 60vh;
        }
    }

    /* Past LG */
    @media (min-width: 769px) {
        #food_accordian{
            bottom: 0;
            left: 0;
            overflow-y: scroll;
            height: 100%;
            width: 50vw;
            transition: all .8s ease-in-out;
        }
    }

    img{
        aspect-ratio: 120/ 70;
        object-fit: cover;
        border-radius: 10px;
    }

    .accordion-button[aria-expanded='true'] {
        background-color: #FFC23F !important;
        color: #1e2e1e;
    }
</style>