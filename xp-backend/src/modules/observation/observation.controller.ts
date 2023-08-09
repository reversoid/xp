import {
  Body,
  Controller,
  Get,
  Post,
  Query,
  Request,
  UseGuards,
  ValidationPipe,
} from '@nestjs/common';
import { CreateObservationDTO } from './dto/create-observation.dto';
import { ObservationService } from './observation.service';
import { GetRandomObservations } from './dto/get-random-observations.dto';
import { AuthGuard } from '../auth/guards/auth.guard';

@Controller('observation')
export class ObservationController {
  constructor(private observationService: ObservationService) {}

  @Post()
  @UseGuards(AuthGuard)
  async createObservation(
    @Request() { user }: { user: any },
    @Body() dto: CreateObservationDTO,
  ) {
    return this.observationService.createObservation(dto, user.id);
  }

  @Get('random')
  @UseGuards(AuthGuard)
  async getRandomObservations(
    @Request() { user }: { user: any },

    @Query(
      new ValidationPipe({
        transform: true,
        forbidNonWhitelisted: true,
      }),
    )
    { amount = 3 }: GetRandomObservations,
  ) {
    return this.observationService.getRandomObservations(amount, user.id);
  }
}
